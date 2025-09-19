# book-app
Webapp to track my reads.


Set Up:
git clone https://github.com/Oscar-Poski/book-app.git
cd book-app/
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt

Run App in Test env:
cd backend/
uvicorn app.main:app --reload