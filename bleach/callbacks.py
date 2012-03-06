"""A set of basic callbacks for bleach.linkify."""


def nofollow(attrs, new=False):
    attrs['rel'] = 'nofollow'
    return attrs


def target_blank(attrs, new=False):
    attrs['target'] = '_blank'
    return attrs
