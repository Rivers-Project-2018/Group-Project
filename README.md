# Group Project
This page summarises the work perfomed as a group and the indivuals.

## 1) Introduction to project Antonia

## 2) Introduction to FEV Model Jack

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
</p>

The figure shown above details the different levels of flood mitigation provided by each mitigation project (RESERVIORS: using reservoirs as storage; NFM: leaky dams; TREES: planting trees). 

## 6) River Irwell, Greater Manchester
Work on the River Irwell can be found at the following link: https://github.com/Rivers-Project-2018/River-Irwell-Mary-Saunders.

## 7) River Avon, Warwickshire

Indepnedent analysis of the River Avon, in Warwickshire (a major tributary of the River Severn) can be found in the linked repository; https://github.com/Abbey-Chapman/River_Avon.

## 8) Ouse

## 9) Wharfe

## 10) Thames, Berkshire

Analysis of the River Thames 2013-2014 flood can be found in the following repository: https://github.com/Rivers-Project-2018/Sophie-River-Thames .

## 11) Conclusion
-Comparison of Rivers
-Further work needed 





