from flask import Flask, request, jsonify
from recipe.scraper import get_recipe_data, get_scraper

app = Flask(__name__)


@app.route("/recipes", methods=["POST"])
def scrape_recipe():

    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": '"url" parameter is required'}), 400

    url = data["url"]

    if not url.startswith("http://") and not url.startswith("https://"):
        return jsonify({"error": f"invalid url format: {url}"}), 400

    scraper, err = get_scraper(url)
    if err:
        return (
            jsonify({"error": f"an error occurred while processing the url: {err}"}),
            500,
        )

    recipe_data, extraction_err = get_recipe_data(scraper)
    if extraction_err:
        return jsonify({"error": extraction_err}), 500

    return jsonify(recipe_data), 200


if __name__ == "__main__":
    app.run(debug=True)
