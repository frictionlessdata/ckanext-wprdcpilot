import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class WprdcpilotPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IFacets)

    def dataset_facets(self, facets_dict, package_type):
        facets_dict['vocab_validation_status'] = toolkit._('Validation status')

        return facets_dict
