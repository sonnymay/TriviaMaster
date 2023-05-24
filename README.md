# TriviaMaster

TriviaMaster is a console-based trivia game that fetches random trivia questions from the Open Trivia Database API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need Python 3.6+ installed on your local machine. You can download it [here](https://www.python.org/downloads/).

Also, the `requests` Python library is used in this project. If not installed, you can do it using pip:

```bash
pip install requests
```

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/sonnymay/TriviaMaster.git
cd TriviaMaster
```

## Running the Application

To run the application, simply use the python command followed by the script name:

```bash
python main.py
```

The program will fetch a trivia question, display it, and wait for your answer. It's case-insensitive, so you don't have to worry about capitalizing your answer correctly.

If you answer correctly, the program will congratulate you. If your answer is wrong, it will display the correct answer.

## Built With

* [Python](https://www.python.org/) - The programming language used
* [requests](https://requests.readthedocs.io/en/master/) - Python library for making HTTP requests
* [Open Trivia Database API](https://opentdb.com/api_config.php) - API for fetching trivia questions

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/yourusername/yourgistid) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

---
