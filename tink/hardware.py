import uuid


class hardware:
    def __init__(self, hw_name, hw_flavor, hw_network, hw_mac, ipmi_ip=None, ipmi_user=None, ipmi_pass=None):
        self.uuid = self.gen_uuid()
        self.name = hw_name
        self.flavor = hw_flavor
        self.network = hw_network
        self.mac = hw_mac
        self.ipmi_ip = ipmi_ip
        self.ipmi_user = ipmi_user
        self.ipmi_pass = ipmi_pass
        self.instance_uuid = None

    def gen_uuid(self):
        return uuid.uuid1()

    def save(self):
        # Call database driver to "Save" this.
        # DB Driver will see if UUID is already present and either insert or update
        pass

    def get(self):
        pass

    def delete(self):
        pass
