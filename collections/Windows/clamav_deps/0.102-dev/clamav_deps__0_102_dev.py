"""
Copyright (C) 2019 Cisco Systems, Inc. and/or its affiliates. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import shutil

from recipes.recipe import BaseRecipe


class Recipe(BaseRecipe):
    """
    Recipe to build clamav.
    """

    name = "clamav_deps"
    version = "0.102"
    collection = True
    dependencies = [
        "curl",
        "json_c",
        "pthreads",
        "libxml2",
        "openssl",
        "pcre2",
        "bzip2=1.0.7",
    ]
