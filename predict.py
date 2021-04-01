import challenge_2021 as tot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
#from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima


#Preparation of the data to be used for prediction
totem = tot.format_name(tot.Load_db().save_as_df(),['Date','Time','Total','Count','U1','U2'])
totem = tot.format_drop(totem, ['U1','U2'])
totem = tot.format_time(totem)
#totem.set_index('Timeused',inplace=True)
#Plotting the bikes passages curve
totem.plot(kind='line',x='Timeused',y='Count',color='blue',)
plt.xlabel('Date')
plt.ylabel('Nombre de vélos')
plt.title('Nombre de vélos par jour entre 00h00 et 09h00 au totem d\'Albert 1er')
plt.legend()
plt.show()

#Using auto_arima algorithm to find the best suitable orders for ARIMA model
stepwise_fit = auto_arima(totem['Count'], trace=True, seasonal=True)
stepwise_fit.summary

#Building the ARIMA model
model = ARIMA(totem['Count'],order=(2,1,1))
model = model.fit()
model.summary()

pred = model.predict(end= len(totem)+1,type="levels").rename('Prediction ARIMA') #The last index printed corresponds to the day we want the prediction for

#Plotting the prediction curve
pred.plot(legend=True)
plt.xlabel('Date')
plt.ylabel('Nombre de vélos')
plt.title('Nombre de vélos par jour entre 00h00 et 09h00 au totem d\'Albert 1er')
plt.legend()
plt.show()
print(pred.tail)

