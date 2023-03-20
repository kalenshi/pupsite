from pupsite import create_site

app = create_site()
if __name__ == "__main__":
    app.run(debug=True, port=5000)
