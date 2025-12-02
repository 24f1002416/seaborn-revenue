import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic monthly revenue data for different customer segments
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create data for three customer segments with realistic seasonal patterns
data = {
    'Month': months * 3,
    'Revenue': [
        # Premium Segment - higher baseline, peak in holiday season
        45000, 47000, 50000, 52000, 54000, 56000,
        58000, 60000, 62000, 65000, 70000, 75000,
        # Standard Segment - moderate baseline, steady growth
        30000, 31000, 32500, 34000, 35000, 36000,
        37500, 39000, 40000, 42000, 45000, 48000,
        # Budget Segment - lower baseline, slight seasonal variation
        18000, 19000, 20000, 21000, 22000, 22500,
        23000, 24000, 25000, 26000, 28000, 30000
    ],
    'Segment': ['Premium'] * 12 + ['Standard'] * 12 + ['Budget'] * 12
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Month to categorical with proper ordering
df['Month'] = pd.Categorical(df['Month'], categories=months, ordered=True)

# Set Seaborn style and context for professional appearance
sns.set_style('whitegrid')
sns.set_context('paper', font_scale=1.2)

# Create figure with specified size for 512x512 output
# Using figsize=(8, 8) with dpi=64 gives exactly 512x512 pixels
fig, ax = plt.subplots(figsize=(8, 8), dpi=64)

# Create lineplot with custom styling
sns.lineplot(
    data=df,
    x='Month',
    y='Revenue',
    hue='Segment',
    marker='o',
    linewidth=2.5,
    markersize=8,
    palette='Set2',
    ax=ax
)

# Add titles and labels
ax.set_title('Monthly Revenue Trend by Customer Segment',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=11, fontweight='bold')
ax.set_ylabel('Revenue ($)', fontsize=11, fontweight='bold')

# Customize legend
ax.legend(title='Customer Segment',
          title_fontsize=10,
          fontsize=9,
          loc='upper left',
          frameon=True)

# Format y-axis to show currency
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# Rotate x-axis labels for better readability
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# Add grid for better readability
ax.grid(True, alpha=0.3, linestyle='--')

# Adjust layout manually to fit within the 512x512 canvas
# Do NOT use tight_layout() as it changes the figure size
fig.subplots_adjust(left=0.12, right=0.95, top=0.93, bottom=0.12)

# Save the chart with exactly 512x512 pixels
# figsize=(8, 8) with dpi=64 produces 8*64 = 512 pixels
plt.savefig('chart.png', dpi=64)

# Close the figure to free memory
plt.close()

print("Chart generated successfully: chart.png (512x512 pixels)")
