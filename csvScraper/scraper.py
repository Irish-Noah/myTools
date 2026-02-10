import csv
import os
import json


with open('input.csv', mode='r') as file:
    reader = csv.DictReader(file)
    signals = []
    for row in reader:
        signals.append(row['header'])


template1 = {
          "name": "can_check_2",
          "operands": [
            {
              "operands": [
                {
                  "flags": [
                    "json-ref"
                  ],
                  "name": "mlev_prob",
                  "source": "can-signal",
                  "param": ','.join(signals)
                },
                {
                  "param": "E#",
                  "source": "const"
                }
              ],
              "operator": "STRSTARTSWITHIC",
              "source": "synth"
            },
            {
              "name": "mlev_prob",
              "source": "ref"
            },
            {
              "param": "Get can Success",
              "source": "const"
            }
          ],
          "source": "synth",
          "operator": "CHECK"
        }

master = {'key':[]}
for signal in signals:
    master['key'].append(
        {
          "name": signal,
          "param": "mlev_prob:" + signal,
          "source": "ref"
        }
    )


output_path = os.path.join(os.path.dirname(__file__), 'bundle.json')

output_path2 = os.path.join(os.path.dirname(__file__), 'data.json')


with open(output_path, 'w') as outfile:
    json.dump(template1, outfile, indent=2)

with open(output_path2, 'w') as outfile:
    json.dump(master, outfile, indent=2)