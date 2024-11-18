# Pair Drawer Application

This application is a simple **Flask-based web app** for registering participants and randomly drawing pairs. The app supports adding, editing, and deleting participants, as well as managing multiple draw rounds.

---

## Features

- **Register Participants**: Add participants to the list.
- **Edit Participants**: Update participant names.
- **Delete Participants**: Remove participants from the list.
- **Perform Draw**: Randomly draw pairs from the list of participants.
- **Exclude Logic**: If there's an odd number of participants, one person will be excluded per round.
- **History Management**: View the history of all drawn pairs.
- **Reset Functionality**: Clear all participants, rounds, and history.

---

## Requirements

- Python 3.9+
- Flask (Install via `pip install flask`)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   Create a virtual environment and install Flask:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install flask
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your browser and go to:
   ```
   http://localhost:8080
   ```

---

## Project Structure

```plaintext
.
├── app.py                # Main Flask application
├── static/
│   └── style.css         # Styles for the web pages
├── templates/
│   ├── index.html        # Homepage
│   ├── cadastro.html     # Registration page
│   ├── editar.html       # Edit participant page
│   ├── sorteio.html      # Pair draw page
├── README.md             # Project documentation
```

---

## Usage

### Homepage
The homepage displays all registered participants and options to:
- Register a new person.
- Perform a draw.
- Reset the list.

### Register Page
Add a new participant by filling in their name.

### Edit Page
Edit the name of an existing participant.

### Pair Draw Page
View the results of the current round, including:
- Pairs formed.
- Any excluded participant.
- A history of all drawn pairs.

### Reset
Reset all data, including participants and draw history.

---

## Example Screenshots

### Homepage
View and manage participants:
![Homepage Example](/assets/home-page.png)

### Draw Page
View drawn pairs and excluded participants:
![Draw Page Example](/assets/draw-page.png)

---

## Future Improvements

- Add support for exporting draw results.
- Implement authentication for managing participants.
- Add themes and customization options.

---

## License

This project is open-source and available under the **MIT License**.

---

Enjoy using the **Pair Drawer Application**! 🎉