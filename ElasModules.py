def elas_modules():
    modules = [
        "bank-info-",
        "cloud-app-",
        "defender-",
        "dhcp-",
        "filebeat-azure-",
        "filebeat-microsoft-",
        "horizon-",
        "vmware-",
        "logs-iis.access-",
        "logs-o365.audit-",
        "logs-sophos.xg-",
        "logs-system.",
        "logs-windows.",
        "logs-zeek."
    ]
    return modules


class ElasModules:
    def __init__(self):
        self.elas_modules = elas_modules()
