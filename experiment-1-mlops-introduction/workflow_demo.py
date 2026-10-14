steps = [
    '1. Define business problem and success metric',
    '2. Collect and version data',
    '3. Validate data and check quality',
    '4. Preprocess and engineer features',
    '5. Train model and record parameters',
    '6. Evaluate against baseline and acceptance criteria',
    '7. Register approved model artifact',
    '8. Deploy model behind a service or batch job',
    '9. Monitor latency, errors, quality and data/model drift',
    '10. Feed monitoring results into controlled retraining',
]
print('MLOps lifecycle workflow')
for step in steps: print(step)
print(f'PASS: displayed {len(steps)} lifecycle stages')
