from geopy.distance import geodesic
from models import Helper
from database import db
import time

MAX_RADIUS_KM = 8

def calculate_score(helper, booking):
    helper_location = (helper.latitude, helper.longitude)
    user_location = (booking.latitude, booking.longitude)

    distance = geodesic(helper_location, user_location).km

    if distance > MAX_RADIUS_KM:
        return -1

    if distance == 0:
        distance = 0.1

    distance_score = (1 / distance) * 0.5
    rating_score = helper.rating * 0.4
    reliability_score = 0.1

    return distance_score + rating_score + reliability_score


def assign_helper(booking):
    helpers = Helper.query.filter_by(
        skill=booking.service_type,
        status="Available"
    ).all()

    best_helper = None
    best_score = -1

    for helper in helpers:
        score = calculate_score(helper, booking)
        if score > best_score:
            best_score = score
            best_helper = helper

    if best_helper:
        best_helper.status = "Busy"
        booking.assigned_helper = best_helper.name
        db.session.commit()
        return best_helper

    return None


def auto_reassign(booking):
    time.sleep(5)
    return assign_helper(booking)
