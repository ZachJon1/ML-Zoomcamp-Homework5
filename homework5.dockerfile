FROM  agrigorev/zoomcamp-model:3.8.12-slim
RUN pip install pipenv
WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --deploy --system
COPY ["*.py", "churn-model.bin", "./"]
EXPOSE 9696
ENTRYPOINT ["waitress", "--listen", "0.0.0.0:9696", "predict_Homework5:app"]