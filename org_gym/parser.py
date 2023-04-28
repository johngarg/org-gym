#!/usr/bin/env python3

from collections import defaultdict
from orgparse import load
import pandas as pd
from datetime import datetime
from typing import List, Tuple
from pint import UnitRegistry

UREG = UnitRegistry()
def parse_exercise(exercise: str) -> List[Tuple[str, str]]:
    """Parse exercise body into a list of (weight, reps) tuples."""
    data = []
    sets = exercise.split("-")[1:]
    for set_ in sets:
        weight, reps = set_.split("x")
        weight = UREG(weight.strip())
        data.append((weight, int(reps.strip())))
    return data

def parse_gym_file(filename: str) -> pd.DataFrame:
    """Return a dataframe of all exercises in a workout org-file, flattened on reps.

    """
    file_ = load(filename)
    training_data = defaultdict(list)
    for workout in file_.children:
        if "skip" in workout.tags:
            continue
        workout_properties = workout.properties
        name = workout.heading
        for exercise in workout.children:
            if "skip" in exercise.tags or exercise.todo in {"TODO", "KILL", "CANC"}:
                continue
            muscle = exercise.get_property("muscle")
            note = exercise.get_property("note")
            for weight, reps in parse_exercise(exercise.body):
                training_data['exercise'].append(exercise.heading)
                training_data['workout'].append(name)
                # Associate workout properties to set
                for k, v in workout_properties.items():
                    training_data[k].append(v)
                # Associate exercise properties to set
                training_data['muscle'].append(muscle)
                training_data['exercisenote'].append(note)

                # Add rep information
                training_data['weight'].append(weight.m)
                training_data['unit'].append(weight.u)
                training_data['reps'].append(reps)

    return pd.DataFrame(training_data)
