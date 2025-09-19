# 📚 Book App

Webapp to track my reads.

---

## 🚀 Set Up

```bash
git clone https://github.com/Oscar-Poski/book-app.git
cd book-app/
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

## Run App in Test Environment

### Start the server
```bash
cd backend/
uvicorn app.main:app --reload
```

# API Usage Examples

Below are some example `curl` commands to interact with the API.

## Health Check
```bash
curl http://127.0.0.1:8000/health
```
## Get All Books
```bash
curl http://127.0.0.1:8000/api/v1/books/
```
## Create Book
```bash
curl -X POST http://127.0.0.1:8000/api/v1/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Architecture","author":"Robert C. Martin","pages":432,"rating":4.5,"notes":"solid principles"}'
```
## Get Book
```bash
curl http://127.0.0.1:8000/api/v1/books/<ID>
```
## Update Book
```bash
curl -X PATCH http://127.0.0.1:8000/api/v1/books/<ID> \
  -H "Content-Type: application/json" \
  -d '{"rating": 5}'
```
## Delete Book
```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/books/<ID>
```