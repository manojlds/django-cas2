def dict_to_querystring(params):
    return "&".join(['%s=%s' % (key, value) for key, value in params.iteritems()])
