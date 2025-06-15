# Bellabeat User-Behavior Case Study

This case study analyzes activity and sleep behavior using Fitbit-derived data to help Bellabeat understand user engagement. Bellabeat is a wellness technology company focused on empowering women through smart devices and personalized health insights. The project uses SQL for data preparation and Python for exploratory data analysis and segmentation.

---

## Objectives

- Detect patterns in daily steps, calories burned, and sleep duration
- Segment users based on engagement to inform marketing strategies
- Recommend improvements to Bellabeat's product experience based on user behavior

---

## Project Structure

```
bellabeat_case_study/
├── data/                 # Cleaned analysis-ready CSVs
├── notebooks/            # Python EDA and clustering notebook
├── reports/              # Executive summary and case study report (PDF)
├── scripts/              # SQL data cleaning and preparation scripts
├── visuals/              # PNGs for report visuals and charts
├── requirements.txt      # Python environment dependencies
```

---

## Tools Used

- SQL for data joins, filtering, and aggregation
- Python (pandas, seaborn, matplotlib) for EDA and visualization
- Scikit-learn for user segmentation (K-means clustering)
- DOCX and PDF for stakeholder-friendly reporting

---

## Key Findings

- 75 percent of users averaged fewer than 8,000 steps per day
- Weekend activity drops by about 1,200 steps compared to weekdays
- 30 percent of nights showed under 6 hours of sleep
- High-engagement users (>10,000 steps and >=7 hours sleep) represented 12 percent of the user base, but 28 percent of sessions
- Step count and calories burned are strongly correlated (Pearson r ≈ 0.76)

---

## Recommendations

- Send motivational nudges to users with fewer than 3,000 steps by noon
- Launch weekend challenges to close the activity drop-off
- Offer mindfulness and sleep content to users with short or inconsistent sleep
- Use badges and streak-based incentives to build consistency
- Target high-engagement users with upsell offers for accessories and premium plans

*Note: Uplift figures mentioned in the executive summary are based on industry benchmarks and should be validated by Bellabeat through A/B testing.*

---

## How to Reproduce

1. Clone the repository
2. Install dependencies from `requirements.txt`
3. Open the notebook in `notebooks/` and run the analysis

---

## Author

Bryce Smith  
GitHub: https://github.com/thebryce15

---

This case study is a personal portfolio project and is not affiliated with Bellabeat Inc.
