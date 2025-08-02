# Installation
```bash
pip install fastapi
pip install "uvicorn[standard]"
```

# Run Application
```bash
uvicorn 01-main:app --reload
```
app: Python module (object in the py file)
<br>--reload: use only for development, not for production

# Automate Generate Documentation
## How to Get the Documentation?
`<url>`/docs

## Query Parameters
Declare other function parameters that are not part of the parameters

## Request Body
When send data from a client to API, send it as request body
| Terms | Definition |
| --- | --- |
| Request Body | Data sent by the client to API |
| Response Body | Data API sent to the client | 