FROM  agrigorev/zoomcamp-model:3.8.12-slim
RUN pip install pipenv
WORKDIR /app
RUN pipenv install --deploy --system
COPY ["*.py", "predict_Homework5", "./"]
EXPOSE 9696
ENTRYPOINT ["gunicorn", "bind", "0.0.0.0:9696", "predict_Homework5:app"]