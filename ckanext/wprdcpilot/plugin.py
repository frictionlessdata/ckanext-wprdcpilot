from collections import OrderedDict

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class WprdcpilotPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IFacets)

    def dataset_facets(self, facets_dict, package_type):

        new_facets = OrderedDict()
        new_facets['vocab_validation_status'] = toolkit._('Validation status')

        new_facets.update(facets_dict)

        return new_facets
