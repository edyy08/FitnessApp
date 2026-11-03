"""Calorie and score. Activity events."""

from __future__ import annotations

MIN_DURATION_SECONDS = 5 * 60  # events shorter than this are discarded
DEFAULT_WEIGHT_KG = 70.0


def is_valid_duration(duration_seconds: float,
                      minimum: int = MIN_DURATION_SECONDS) -> bool:
    return duration_seconds >= minimum


def calories_burned(met: float, weight_kg: float, duration_seconds: float) -> float:
    """kcal = MET x weight(kg) x hours."""
    return round(met * weight_kg * (duration_seconds / 3600.0), 1)


def activity_score(duration_seconds: float, score_multiplier: float) -> float:
    """One point per active minute, weighted by activity type.

    A small bonus rewards longer sessions: +10 % past 30 min, +20 % past 60.
    """
    minutes = duration_seconds / 60.0
    bonus = 1.2 if minutes >= 60 else 1.1 if minutes >= 30 else 1.0
    return round(minutes * score_multiplier * bonus, 1)
