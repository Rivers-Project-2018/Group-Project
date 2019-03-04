# Group Project
This page summarises the work perfomed as a group and the individuals.

## 1) Introduction

Climate change is increasing the frequency of extreme rainfall and flooding internationally. [1]

In the north of the UK alone, 17,000 properties were affected by flooding in the winter 2015-2016. December 2015 has been reported as the wettest month ever recorded. In 2017, flooding was a natural hazard identified as a major threat to the UK on the UK’s Risk Register. [2,3]

In the UK, cities and local councils are often responsible for designing flood management plans with the support of regional divisions of goverment organisations such as the Environmental Agency. Evidence based decision making is needed inorder to optimise the limited resources available to local authorities. 

## 2) Introduction to FEV Model

When planning flood mitigation, it is important to estimate the volume of water that the river will flood by, in order to see which flood alleviation schemes are most appropriate. We call this the flood excess volume (FEV). 

To calculate the FEV of a flood, first data must be collected and analyzed from the Environmental Agency. They analyze the river level (height) against a timestamp usually at 15 minute intervals across hundreds of gauge stations over the country. For each individual gauge station, it is possible to estimate the threshold level of the river *h<sub>T</sub>*, measured in m. This value can be estimated many different ways, from social media time stamped photos to online live resources such as (www.gaugemap.com). 

To analyze this data, a rating curve is created by the Environmental Agency to estimate the flow of water m<sup>3</sup>/s at the river’s given level and time. The frequent measurements taken at the gauge station can then be plotted onto a graph using the rating equation Q=Q(h), where Q is the flow of water m<sup>3</sup>/s. We can then apply *h<sub>T</sub>* into the rating curve to give the threshold flow *q<sub>T</sub>*=Q(*h<sub>T</sub>*). FEV, or Ve can then be defined as the integral of Q(t)-*q<sub>T</sub>* over time *T<sub>f</sub>*, where *T<sub>f</sub>* is where Q(t)-*q<sub>T</sub>*>0. Ve is measured in m<sup>3</sup>. This gives a volume of water in which the river has flooded by. A way to estimate this value is to evaluate *h<sub>M</sub>*, the mean level of the river given the level is above *h<sub>T</sub>*. Again, this value can be applied into the rating equation to give a flow value *q<sub>M</sub>*. Thus,

![Screen Shot 2019-03-04 at 14.38.53.png](https://github.com/Rivers-Project-2018/Jack-Willis/blob/master/Screen%20Shot%202019-03-04%20at%2014.38.53.png).

This is the formula that will be used to estimate FEV from the quadrant plots that have been created for each river.

## 3) Familarisation with FEV Model

### i) The River Don, Sheffield

Substantial flooding occured early in the month of July, 2007, in the West Yorkshire city of Sheffield. Below is a graph illustrating the behaviour of the River Dons height throughout the year 0f 2007, using height data gathered from the Sheffield Hadlands gauging station.
 
![Don-Long_Time_Graph.png](https://github.com/Rivers-Project-2018/Group-Project/blob/master/Don-Long_Time_Graph.png)

*Height levels for the River Don in the Sheffield Hadlands throughout the year 2007.*
 
It is therefore clear that the July 2007 flooding event was a rare event. Indeed, a height greater than 2m was only achieved at one other point for the entire year, and even then the height only reached around 3m whilst the flooding event in July 2007 achieved a maximum height nearing 5m. This kind of flood is said to have a 1:200-year-return period; that is, a flood of this magnitude only occurs with 0.5% probability each year.

In order to calculate the volume of water discharged during the flooding event (the FEV), the plotting of the below quadrant graph is necessary. The threshold height of 2.9m is chosen. This is because, whilst https://www.gaugemap.co.uk/ states that flooding is possible from 2.63m upwards, the supervisors of this project have had prior experience with the River Aire and Calder suggesting that this level is too low. Hence the threshold height is estimated to be 2.9m.
 
![Don-Quadrant_Graph](https://github.com/Rivers-Project-2018/Group-Project/blob/master/Don-Quadrant_Graph.png)

*Quadrant plot analysing the July 2007 flooding event in Sheffield*

Because of the severity of this flood, the Sheffield City Council have investigated the implementation of various flood mitigation measures, with an emphasis on Natural Flood Mitigation measures, in particular flow attenuation features such as leaky dams. They are also looking into the possibility of drawing down various drinking water reservoirs that are already built along the River Don with the aim of increasing their floodwater storage potential. Further information on the study performed by the Sheffield City Council can be found in www.floodprotectionsheffield.com.

### ii) River Aire, Leeds

One of the floods we looked at was the Boxing Day flood of the River Aire in Leeds in 2015, using data taken from the monitoring station at Armely by the Environment Agency. Taking a threshold height of 3.9m above which flooding occured, we were able to produce the following quadrant plot using Python or R. This threshold height was estimated by Professor Bokhove by looking at photographs of the local area, along with their timestamps.

![airepythongraph](https://github.com/Rivers-Project-2018/Group-Project/blob/master/airepythongraph.png)

The lower left quadrant the relationship between the river height and time, the upper right quadrant shows time against flow, and the upper left quadrant contains a rating curve with a linear approximation. The dashed lines indicate a threshold height *h<sub>T</sub>* and the mean height of the flood *h<sub>m</sub>*, and their respective flow rates *Q<sub>m</sub>* and *Q<sub>T</sub>*. Using these values we were able to calculate the FEV as 9.34 Mm<sup>3</sup>, with *T<sub>f</sub>* (the duration of the flood) being 32 hours.

The Leeds Flood Alleviation Scheme was put into place to help avoid damage of this extent happening again. One scenario from Phase II of the scheme involves building flood walls of a height of varying heights in the city centre. This would help prevent flooding here, however could cause flooding downstream. Therefore a floodplain further upstream would help to counteract this. A graphical representation of the flood walls and the Calverley flood plain is as follows:

![airesquarelake1](https://github.com/Rivers-Project-2018/Group-Project/blob/master/airesquarelake1.png)

This shows that 8% of the FEV would be mitigated by the floodplain, with the remaining 92% by the city centre flood walls. It also shows the cost-effectiveness of the mitigation strategy - £0.75M per 1% of FEV mitigated, which includes £10M for the storage area, and £65M for the flood walls.

### iii) River Calder, Mytholmroyd, Yorkshire

Lastly, we focused on the River Calder flood that took place on Boxing Day in 2015. The given data was from the Mytholmroyd station.

<p align="center">
  <img width="500" height="500" src="https://github.com/Rivers-Project-2018/Group-Project/blob/master/SophiesCalderRecreation.png">
</p>

<p align="center">
  <img width="500" height="500" src="https://github.com/Rivers-Project-2018/Group-Project/blob/master/Sophies_FEV_mitigation_plot_recreation_for_Calder.png">
   <figcaption>Figure 6: Flood-excess lake for Calder</figcaption>
</p>

## 6) River Irwell, Greater Manchester
Work on the River Irwell can be found at the following link: https://github.com/Rivers-Project-2018/River-Irwell-Mary-Saunders.

## 7) River Avon, Warwickshire

Indepnedent analysis of the River Avon, in Warwickshire (a major tributary of the River Severn) can be found in the linked repository; https://github.com/Abbey-Chapman/River_Avon.

## 8) River Ouse, York
Analysis on the River Ouse in York for the flood events in 2000 and 2015 can be found in the following repository: https://github.com/Rivers-Project-2018/River_Ouse_Antonia

## 9) River Wharfe, Addingham

Below is the quadrant plot for the River Wharfe at Addingham, from the boxing day floods in 2015.

![Addingham Quadrant Plot Final(1).png](https://github.com/Rivers-Project-2018/Jack-Willis/blob/master/Addingham%20Quadrant%20Plot%20Final%20(1).png)

Currently there is a large flood alleviation programme taking place on the River Wharfe, with many mitigation schemes explored by the Leeds City Council. Some of these schemes for example are:

![Screen Shot 2019-03-04 at 15.13.52.png](https://github.com/Rivers-Project-2018/Jack-Willis/blob/master/Screen%20Shot%202019-03-04%20at%2015.13.52.png)

*Data collected by the Leeds City Council (https://www.leeds.gov.uk/docs/Otley%20FAS%20Drop%20In%20Material%20-%2021%20June%202018.pdf).*


## 10) Thames, Berkshire

Analysis of the River Thames 2013-2014 flood can be found in the following repository: https://github.com/Rivers-Project-2018/Sophie-River-Thames .

## 11) Conclusion
-Comparison of Rivers
-Further work needed 

## 12)References 
1.European Academics Society Advisory Council.New data confirm increased frequency of extreme weather events, European national science academies urge further action on climate change adaptation.[Online].2018.[Accessed 4 March 2019]. Available from:https://easac.eu/press-releases/details/new-data-confirm-increased-frequency-of-extreme-weather-events-european-national-science-academies/ 
2. Environmental Agency. Climate change means more frequent flooding, warns Environment Agency.[Online].2018.[Accessed 2 January 2019]. Available from: https://www.gov.uk/government/news/climate-change-means-more-frequent-flooding-warns-environment-agency
3. UK Government. National Risk Register Of Civil Emergencies 2017 Edition. [Online].2017.[Accessed 2 January 2019]. Available from: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/644968/UK_National_Risk_Register_2017.pdf





