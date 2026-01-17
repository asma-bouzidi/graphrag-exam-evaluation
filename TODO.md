# TODO: Fix 500 Internal Server Error on /api/exams/upload

## Completed Fixes:
1. ✅ Changed upload directory from `/app/uploads` to `./uploads` (Permission fix)
2. ✅ Changed OpenAI model from `gpt-5-nano` to `gpt-4o-mini` (Invalid model fix)
3. ✅ Removed `gpt-5-nano` from reasoning models list

## Remaining Issues to Fix:

### System Dependencies:
- [ ] Install Tesseract OCR for image processing
- [ ] Install poppler-utils for PDF to image conversion
- [ ] Install libmagic for file type detection

### Environment Variables:
- [ ] Ensure OpenAI API key is set
- [ ] Create .env file with required variables

### Docker/Service Issues:
- [ ] Check if Neo4j is running
- [ ] Verify upload directory permissions

### Code Fixes:
- [ ] Update remaining test files to use valid model name
- [ ] Add better error handling for missing dependencies

## Commands to Run:
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-fra poppler-utils libmagic1

# Create upload directory
mkdir -p backend/uploads
chmod 755 backend/uploads

# Set environment variables
export OPENAI_API_KEY="your-api-key-here"
export OPENAI_MODEL="gpt-4o-mini"

# Start Neo4j
docker-compose up -d neo4j
