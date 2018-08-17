from unittest import TestCase
import os
from niftynet.utilities import NiftyNetLaunchConfig


class IniYamlEquivalenceTest(TestCase):

    @classmethod
    def setUpClass(cls):
        config_files_dir = os.path.join(
            os.path.split(__file__)[0], '..', 'config'
        )
        config_file = 'default_segmentation'
        cls.ini_file = os.path.join(
            config_files_dir, '{}.ini'.format(config_file)
        )
        cls.yaml_file = os.path.join(
            config_files_dir, '{}.yml'.format(config_file)
        )

    def setUp(self):
        self.ini_config = NiftyNetLaunchConfig()
        self.yaml_config = NiftyNetLaunchConfig()

    def test_read_ini_equivalent_to_read_yaml(self):
        # TODO
        raise NotImplementedError

    def test_incompatible_file_not_read(self):
        self.ini_config.read(IniYamlEquivalenceTest.ini_file)
        with self.assertRaises(ValueError):
            self.ini_config.read(IniYamlEquivalenceTest.yaml_file)

        self.yaml_config.read(IniYamlEquivalenceTest.yaml_config)
        with self.assertRaises(ValueError):
            self.yaml_config.read(IniYamlEquivalenceTest.ini_file)

    def test_sections_same(self):
        # TODO
        raise NotImplementedError

    def test_items_same(self):
        # TODO
        raise NotImplementedError

    def test_add_section_same(self):
        # TODO
        raise NotImplementedError

    def test_set_same(self):
        # TODO
        raise NotImplementedError

    def test_remove_section_same(self):
        # TODO
        raise NotImplementedError

    def has_section_same(self):
        # TODO
        raise NotImplementedError