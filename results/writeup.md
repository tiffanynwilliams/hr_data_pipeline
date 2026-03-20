1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates 

According to the "Target HR Zone 50-85%", the phase1.txt file shown the most active period. I say so, because the average of all the heartrates was the highest at 87.3 bpm. The data can support two hypotheses: the participant is healthier than the average or purposefully not exerting as much energy. Their heartrates are slightly lower than the range expected of those in their 30s.

2) Which file had the **poorest** data quality? How do you know?

I printed out the removed_vals which were non-digit or malformed heartrate values in the data list. The file that had the most was the phase0.txt with 3 malformed heartrates.


3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.

range = max - min
max = 180, min = 68
range = 180 - 68
range = 112

The range is 112 bpm (though, I am unsure if that is the right unit for range).

b) Explain how the extreme value affects the range.

The extreme value affects increases the range, making the spread of the data larger. This makes the data less accurate and could lead to assumptions about healthy ranges of heartrates. 


c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?

Interquartile Range (IQR) allows for a more accurate representation of variability of datasets. Considering that we are analysing heartrate data that allows for a large range, we should use IQR. Unlike the range, the IQR only looks at the middle of the data to eliminate any outliers. 