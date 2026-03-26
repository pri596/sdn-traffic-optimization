def map_intent_to_qos(intent):
    """
    Maps traffic intent to QoS priority and queue.
    :param intent: string, one of "REAL_TIME", "BULK", "BACKGROUND"
    :return: dict with 'priority' and 'queue'
    """
    policy = {
        "REAL_TIME": {"priority": 3, "queue": 0},   # Highest priority
        "BULK": {"priority": 2, "queue": 1},        # Medium priority
        "BACKGROUND": {"priority": 1, "queue": 2}   # Lowest priority
    }

    # Default to background if unknown intent
    return policy.get(intent, {"priority": 1, "queue": 2})
