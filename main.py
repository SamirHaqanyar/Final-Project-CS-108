#Samir Haqanyar
import matplotlib.pyplot as plt
import statistics 
with open("Housing.csv") as dataFile: # open the file
  myData = dataFile.readlines()[1:] # get access to the lines of data
  x = []
  y = []
  prices = []
  areas = []
  bedrooms =[]
  bathrooms = []
  floors = []
  fcount = 0
  unfcount = 0
  scount = 0

choice = input("Select from the choices\n1. Compare house prices with area amount\n2. Basic statistical Summary of the Dataset\n3. Prices for Different Furnishing Statuses\n4. Filter by price range\n5. Filter by area range in square feet\n")
for line in myData: # go through the file, line by line

  line = line.strip() # removes whitespace/newlines before and after
  price, area,bedr,bath,stories,airconditioning,parking,prefarea,furnishingstatus = line.split(",")
  price = int(price)
  prices.append(price)
  area = int(area)
  areas.append(area)
  bedr = int(bedr)
  bedrooms.append(bedr)
  bath = int(bath)
  bathrooms.append(bath)
  stories = int(stories)
  floors.append(stories)
  
  if choice == "1":
    x.append(price)
    y.append(area)
    #https://stackoverflow.com/questions/42223587/how-to-add-title-and-xlabel-and-ylabel
    plt.title("Area over Price")
    
    plt.xlabel("Price in 10 millions (example 1.0 = 10 mil)")
    plt.ylabel("Area in sq Feet")
    
    
    
    
    
  if choice == '3':
    y.append(price)
    if furnishingstatus == "furnished": #checks for furnishing status and counts
      x.append(furnishingstatus)
      fcount+=1
    if furnishingstatus =="semi-furnished":
      x.append(furnishingstatus)
      scount+=1
    
    if furnishingstatus =="unfurnished":
      x.append(furnishingstatus)
      unfcount+=1

            
          
if choice == "1":
  plt.scatter(x, y)
  
  plt.show()
if choice =="2":
  # https://www.w3schools.com/python/ref_stat_mean.asp
  print("Average Price: $"+str(statistics.mean(prices)))
  print("Median price: $"+str(statistics.median(prices)))
  print("Average Area:",statistics.mean(areas),"\nMedian Area:", statistics.median(areas))#literally wasted my time then found this code, hope you don't dock points for shortcuts
  print("Most Frequent number of Bedrooms: ",statistics.mode(bedrooms))
  print("Most Frequent number of Bathrooms: ",statistics.mode(bathrooms))
  print("Most Frequent number of Stories",statistics.mode(floors))
  
if choice =="4":
    min_Choice = int(input(f'Input your minimum starting price (minimum price is {min(prices)})')) 

    max_Choice = int(input(f'Input your maximum price(maximum price is {max(prices)})'))# https://stackoverflow.com/questions/73952981/creating-a-program-that-lets-the-user-input-a-maximum-and-minimum-value-then-let (learned the f'' from there)
  
    filtered_prices = (price for price in prices if min_Choice <= price <= max_Choice) # learned from here https://www.w3schools.com/python/python_lists_comprehension.asp

    if filtered_prices:
      print(f'Filtered prices between ${min_Choice} and ${max_Choice}:') 
      for price in filtered_prices:
          print("$"+str(price))
    else:
      print(f'No prices found between ${min_Choice} and ${max_Choice}.')

if choice =="5":
  min_Choice = int(input(f'Input your minimum area (minimum area is {min(areas)})')) 

  max_Choice = int(input(f'Input your maximum area(maximum area is {max(areas)})'))
  filtered_areas = (area for area in areas if min_Choice <= area <= max_Choice)

  if filtered_areas:
    print(f'Filtered prices between ${min_Choice} and ${max_Choice}:')
    for area in filtered_areas:
        
         print("Areas:",area)
      
  else:
    print(f'No area found between {min_Choice} and {max_Choice}.')
    

  
if choice == "3":
  plt.ylabel('Price in 10 millions')
  plt.title('Price Vs Furnising Status')
  plt.bar(x, y)
  plt.show()

  
