#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the terms of the MIT license.

import re
import sys

from pydistman import DistManager


class Derived(DistManager):
    """docstring for Derived"""
    pass

try:
    cmd = sys.argv.pop(1)
except IndexError:
    cmd = 'build'

dist_name = "freecell_solver"

obj = Derived(
    dist_name=dist_name,
    dist_version="0.4.0",
    project_name=dist_name,
    project_short_description="Freecell Solver bindings",
    release_date="2021-11-26",
    project_year="2020",
    aur_email="shlomif@cpan.org",
    project_email="shlomif@cpan.org",
    full_name="Shlomi Fish",
    github_username="shlomif",
    filter_test_reqs=True,
)
obj.run_command(cmd=cmd, args=[])
