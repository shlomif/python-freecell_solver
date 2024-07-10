#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under the terms of the MIT license.

from pydistman import DistManager


class Derived(DistManager):
    """docstring for Derived"""
    pass


dist_name = "freecell_solver"

obj = Derived(
    dist_name=dist_name,
    dist_version="0.6.0",
    project_name=dist_name,
    project_short_description="Freecell Solver bindings",
    release_date="2024-07-10",
    project_year="2020",
    aur_email="shlomif@cpan.org",
    project_email="shlomif@cpan.org",
    full_name="Shlomi Fish",
    github_username="shlomif",
    filter_test_reqs=True,
)
obj.cli_run()
