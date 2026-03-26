class SDNController:
    def apply_policy(self, flow):
        """
        Simulate SDN controller applying priority and queue rules.
        """
        print(f"[SDN SIMULATION] Flow {flow['src_ip']} -> {flow['dst_ip']} "
              f"assigned priority {flow['priority']} and queue {flow['queue']}")
        # You can add more logic if needed, like routing paths or congestion simulation
        return {"status": "ENFORCED", "path": "LOW_LATENCY_PATH" if flow["priority"] == 3 else "NORMAL_PATH"}
