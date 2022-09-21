FROM python:3.9.5-slim

WORKDIR /e_tickets_app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD streamlit run app.py --server.port $PORT