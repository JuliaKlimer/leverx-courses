class Version:
    def __init__(self, version):
        self.version = self.formatting(version)

    def __eq__(self, other):
        return self.version == other.version

    def formatting(self, version: str):
        for versions in version:
            if versions.find('-', 'alpha', 'beta', 'rc', 'b'):
                return version.replace(versions, '')

    def __lt__(self, other):
        version_1 = self.version.split('.')
        version_2 = self.version.split('.')
        minimum_length = min(len(version_1), len(version_2))
        if version_1[:minimum_length] == version_2[:minimum_length]:
            if len(version_1) < len(version_2):
                return True
        else:
            for elements in range(minimum_length):
                if int(version_1[elements]) > int(version_2[elements]):
                    return False
                elif int(version_1[elements]) < int(version_2[elements]):
                    return True
        return False

def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()