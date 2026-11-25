from website import createa_app

app = createa_app()

if __name__ == '__main__':   
    app.run(debug=True, port=5001)

