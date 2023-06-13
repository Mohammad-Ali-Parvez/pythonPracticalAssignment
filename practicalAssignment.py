import os.path
import csv

def getConversionData(indexNumber, typeOfData, number_to_convert):  # this is to get the final conversion
    conversationRate = ratesArray[indexNumber][typeOfData]
    convertData = conversationRate * float(number_to_convert)
    return convertData

def findAverageValue(data):  # find the average
    avg = sum(data) / len(data)
    return avg

def readCSVFIle():  # convert input csv file to array and save to another csv with average, highest and lowest data

    input_message = "Give name of the data file: "

    fileName = input(input_message)

    file_exists = os.path.exists(fileName)

    if (file_exists):  # if file exists

        with open(fileName, 'r', newline='') as csvFile:
           
            data = csv.reader(csvFile, delimiter=';')
            
            responseText = "Data loaded successfully!\n"

            # This skips the first row of the CSV file.

            next(data)

            # start making array of data

            DATES_DATA = []

            USD_EUR_DATAS = []

            USD_AUD_DATAS = []

            USD_GBP_DATAS = []
            
            for row in data:
                date = row[0]

                DATES_DATA.append(date)

                if row[1] != '':
                    USD_EUR = float(row[1])
    
                    USD_EUR_DATAS.append(USD_EUR)

                if row[2] != '':
                    USD_AUD = float(row[2])
    
                    USD_AUD_DATAS.append(USD_AUD)

                if row[3] != '':
                    USD_GBP = float(row[3])
    
                    USD_GBP_DATAS.append(USD_GBP)

            total_data = len(DATES_DATA)

            if (total_data > 0):
                startDate = DATES_DATA[0]
                endDate = DATES_DATA[total_data - 1]


                highest_of_usd_eur = max(USD_EUR_DATAS)
                average_of_usd_eur = findAverageValue(USD_EUR_DATAS)
                lowest_of_usd_eur  = min(USD_EUR_DATAS)
            
                highest_of_usd_aud = max(USD_AUD_DATAS)
                average_of_usd_aud = findAverageValue(USD_AUD_DATAS)
                lowest_of_usd_aud  = min(USD_AUD_DATAS)
                
            
                highest_of_usd_gbp = max(USD_GBP_DATAS)
                average_of_usd_gbp = findAverageValue(USD_GBP_DATAS)
                lowest_of_usd_gpb = min(USD_GBP_DATAS)
                
                averageDataArray = [average_of_usd_eur, average_of_usd_aud, average_of_usd_gbp]

                highestDataArray = [highest_of_usd_eur, highest_of_usd_aud, highest_of_usd_gbp]

                lowestDataArray = [lowest_of_usd_eur, lowest_of_usd_aud, lowest_of_usd_gpb]

                finalArray = {}
                finalArray[0] = averageDataArray
                finalArray[1] = highestDataArray
                finalArray[2] = lowestDataArray
                
            responseText += "Currency exchange data is from " + f'{total_data}' + " days between " + f'{startDate}' + " and " + f'{endDate}.\n'
            print(responseText)
            
            return finalArray

    else:
        print('No File Exsits with Filename: ' + fileName)


# start of the project

project_introducton_text = "ACME(tm) US DOLLAR EXCHANGE RATE APP\n";

options = {

            1:'LOAD currency exchange rate data from a file',

            2:'USE AVERAGE exchange rate',

            3:'USE HIGHEST exchange rate',

            4:'USE LOWEST exchange rate',

            5:'CONVERT USD TO EUR',

            6:'CONVERT USD TO AUD',

            7:'CONVERT USD TO GBP',

            0:'QUIT program'

};

user_input = ''

# loop through all of the option

for index, item in enumerate(options):

    project_introducton_text += f'{item}) ' f'{options[item]} \n'

project_introducton_text += "Choose what to do: "

conversationRateType = 0

ratesArray = [];

while True:

    user_input = input(project_introducton_text)  # input the option from user

    if (int(user_input) == 0):
        exit()

    elif (int(user_input) == 1):
        ratesArray = readCSVFIle()
    elif ((int(user_input) == 2)):
        conversationRateType = 0
        print('Using the average currency exchange rate.\n')

    elif ((int(user_input) == 3)):
        conversationRateType = 1
        print('Using the highest currency exchange rate.\n')

    elif ((int(user_input) == 4)):
        conversationRateType = 2
        print('Using the lowest currency exchange rate.\n')

    else:
        
        input_text_convert = "Give USD to convert: "
        number_to_convert = input(input_text_convert)  # input the value to convert currency

        output_text_convert = ''

        if ((int(user_input) == 5)):
            convertData = getConversionData(conversationRateType, 0, number_to_convert)
            output_text_convert = f'{float(number_to_convert)} USD in EUR is {round(convertData, 2)} EUR \n'
            
        elif ((int(user_input) == 6)):

            convertData = getConversionData(conversationRateType, 1, number_to_convert)
            output_text_convert = f'{float(number_to_convert)} USD in AUD is {round(convertData, 2)} AUD \n'

        elif ((int(user_input) == 7)):

            convertData = getConversionData(conversationRateType, 2, number_to_convert)
            output_text_convert = f'{float(number_to_convert)} USD in GBP is {round(convertData, 2)} GBP \n'

        print(output_text_convert)  # print the output

    #print('\n')
