#!/bin/bash
echo "======================================"
echo " Running Pytest Automation Suite"
echo "======================================"

# Activate virtual environment (if using one)
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "✅ Virtual environment activated."
else
    echo "⚠️ No virtual environment found. Using system Python."
fi

# Clean old reports
rm -rf reports
mkdir reports

# Generate timestamp for report
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

# Run pytest with HTML report
pytest -v -s --html=reports/report_$timestamp.html --self-contained-html

echo "======================================"
echo "✅ Tests Completed!"
echo "📄 Report generated at: reports/report_$timestamp.html"
echo "======================================"
