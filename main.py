from flask import Flask, request, jsonify

app = Flask(__name__)

# Your details
FULL_NAME = "harshita_jangde"
DOB = "01012000"   # ddmmyyyy
EMAIL = "harshita@example.com"
ROLL_NUMBER = "22BCE10107"

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        input_data = request.json.get("data", [])

        numbers, alphabets, specials = [], [], []

        for item in input_data:
            if item.isdigit():  # pure number
                numbers.append(item)
            elif item.isalpha():  # pure alphabets
                alphabets.append(item.upper())
            elif item.isalnum():  # alphanumeric mix (like ABcD, DOE)
                alphabets.append(item.upper())
            else:  # special chars
                specials.append(item)

        # Even and odd numbers (still as strings)
        evens = [n for n in numbers if int(n) % 2 == 0]
        odds = [n for n in numbers if int(n) % 2 != 0]

        # Sum of numbers as string
        num_sum = str(sum(int(n) for n in numbers))

        # Concatenated alphabets in reverse order, alternating caps
        concat = "".join(alphabets[::-1])
        alt_caps = "".join(
            c.lower() if i % 2 else c.upper()
            for i, c in enumerate(concat)
        )

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odds,
            "even_numbers": evens,
            "alphabets": alphabets,
            "special_characters": specials,
            "sum": num_sum,
            "concat_string": alt_caps
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400


if __name__ == "_main_":
    app.run(debug=True)