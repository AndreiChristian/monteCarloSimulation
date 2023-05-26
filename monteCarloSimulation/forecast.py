import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Monthly sales data for the past year (in number of items sold per month)
sales_data = np.array([100, 120, 130, 150, 170, 180, 190, 170, 165, 140, 110, 100])

# Convert to pandas series
sales_series = pd.Series(sales_data, index=pd.date_range(start='1/1/2022', periods=12, freq='M'))

# Fit ARIMA model
model = ARIMA(sales_series, order=(1, 1, 0))
model_fit = model.fit()

# Get forecast for next year
forecast_object = model_fit.get_forecast(steps=12)

# Extract forecast, standard error and confidence intervals
forecast = forecast_object.predicted_mean
stderr = forecast_object.se_mean
conf_int = forecast_object.conf_int()

# Print forecasted sales for next year
print(forecast)
