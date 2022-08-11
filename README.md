# Predicting Terrorism in the Middle East

## [Final Presentation ]([(https://public.tableau.com/app/profile/frederik.n.lindsey/viz/terrorism_attribution_captstone_viz/Predictors)]) 

## Project Overview: 
- This project takes an in depth look at terrorism in Middle Eastern countries and how it has evolved since 2001. In this project, my team and I analyze information from the Global Terrorism Database and build machine learning models to determine what groups are most at risk of being attacked in the Middle East, as well as attempt to accredit previously unattributed attacks.

## Executive Summary: 
- In our data, we discovered that terrorist attacks in the Middle East increased between 2001 and 2014, utilizing bombing and explosive attacks followed by armed assault, hostage taking, and assassinations. The areas of most attacks were Iraq, Afghanistan, and Pakistan with most active terrorist groups between 2001 and 2017 being ISIL, Al-Qaida, and the Taliban. Finally we discovered the primary targets of these attacks who were the police, the military, private citizens/property, and general government organizations/facilities.

- Finally, we created an array of ML Classification models that predicted who's at risk with 47% accuracy, beating baseline by 75%. Also we predicted the perpetrators of unattributed and unknown attacks at 94% accuracy out performing baseline by over 2.5 times.

## Project Key Takeaways: 
- Terrorist attacks have increased in frequency from 2001- 2014, with a sharp increase occuring from 2011 - 2014. After 2014, there began to be a decline in frequency.
- The most active terrorist groups are ISIL, Al-Qaida, and the Taliban.
- Iraq has had the most active terrorist attacks with over 1600 attacks in 2017 alone, followed by Afghanistan with 862 attacks, and Pakistan with 504 attacks.
- The most targeted groups of people were the police, the military, private citizens/property, and general government.
  - Most, if not all, terrorist groups targeted these groups of people in some way.
- The most prominent type of attacks have been bombing and explosive attacks, followed by armed assault, hostage taking, and assassinations.
  - Historically, bombings resulted in the largest amount of wounded people by a large margin. Second to bombing, unarmed assault would be the leading cause of wounded individuals.

## Deliverables: 
- Final notebook with research process, well-labeled visualizations, models, and key findings. 
- Link to Google Slides presentation
- Link to Tableau Dashboard
- Final presentation

## Project Goals: 
- Analyze the terrorist attacks recorded in the Global Terrorism Database that occured in Middle Eastern Countries from 2001-2017. 
- Investigate the modus operandi of the terrorist groups during the exploratory phase. 
-  Use information gathered in exploration to develop machine learning models that accredit unattributed attacks and predict which groups are most at risk of being attacked.

## Project Plan:
- Acquire the data from the Global Terrorism Database and store the function in the wrangle.py file. 
- Clean the data with functions found in the wrangle.py file. 
- Explore the data and ask questions to clarify what is actually happening. 
  - Ensure to properly annotate, comment, and use markdowns. 
  - Store functions in the utilities.py file for reproducability. 
  - Visualize the data when applicable. 
  - Verify possible relationships using statistical testing. 
- Create Decision Tree models, Random Forest Models, and KNN models to:
  - Predict what groups are most likely to be attacked.
  - Accredit unattributed attacks. 
- Run the best performing models through test. 
- Create a slideshow and Tableau dashboard that is suitable for a general audience. 
- Present information to a general audience. 

## Data Dictionary:
|Term | Description|
|---|---|
| eventid | identification number of the attack|
| year | year that the attack happened|
| month | month that the attack happened|
| day | day that the attack happened|
| country | country where the attack happened| 
| region | overall region where the attack occurred| 
| provstate | province/ state where the attack occured|
| city | city where the attack occured |
| latitude | latitude coordinate where the attack occured| 
| longitude| longitude coordinate where the attack occured| 
| success | binary indicator of whether the attack was successful|
| suicide | binary indicator of whether or not the attack ended in a suicide| 
| attack_type | type of attack that was launched|
| target | broad group of people targeted by the attack|
| targ_desc | broad description of the group that was being attacked|
| targeted_group | specific group being attacked|
| tg_desc | specific description of the group being attack|
| nationality | nationality of the group being attacked| 
| atk_group | terrorist group that launched the attack|
| claimed | indicator of whether or not the attack was claimed|
| weap_type | broad description of weapon that was used|
| weap_sub | specific description of weapon being used|
| killed | number of non-terrorist persons killed in the attack|
| us_killed | number of United States citizens killed in the attack|
| ter_killed | number of terrorist killed in the attack|
| wounded | number of non-terrorist persons wounded in the attack|
| us_wounded | number of United States citizens wounded in the attack|
| ter_wounded | number of terrorist wounded in the attack|
| property | binary indicator of whether or not property was involved in the attack|

## Conclusion
- We were able to maneuver through 2001 and 2017 terrorism data to find out:
  - Who was most at rist of terrorist attacks
  - Who were the most likely perpetrators of the unattributed attacks
- To do this, we created an array of Machine Learning models which ultimately lead to the Decision Tree Classifier and Random Forest yielding the best results. 

- In regards to finding "Who were most at risk of terrorist attacks" and the Random Forest Model we achieved:
  - 52% Accuracy on Training In-Sample Data
  - 47% Accuracy on Test Out-of-Sample Data

- As for the finding "Who were most likely the perpetrators of unattributed attacks, we achieved:
  - 94% Accuracy on Training In-Sample Data
  - 93% Accuracy on Test Out-of-Sample Data

## Our Next Steps:
  - We find benefit in fitting more terrorist groups in our model for discovering the perpetrators of unattributed attacks as, while generally accurate, could use the features for better decision making and precision. 

  - Lastly, To take this project further, we would like to recreate the project on the scale of Global Terrorism. 
