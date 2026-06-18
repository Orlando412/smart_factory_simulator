class OEEMetrics:

    @staticmethod
    def calculate(
        runtime,
        downtime,
        good_units,
        total_units,
        cycle_time,
        elapsed_time
    ):

        availability = (
            runtime /
            (runtime + downtime)
            if runtime + downtime > 0 else 0
        )

        quality = (
            good_units / total_units
            if total_units > 0 else 0
        )

        performance = (
            (total_units * cycle_time) /
            elapsed_time
            if elapsed_time > 0 else 0
        )

        oee = (
            availability *
            quality *
            performance
        )

        return {
            "availability": round(availability * 100, 2),
            "performance": round(performance * 100, 2),
            "quality": round(quality * 100, 2),
            "oee": round(oee * 100, 2)
        }