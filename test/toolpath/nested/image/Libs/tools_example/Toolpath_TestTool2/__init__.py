# SPDX-License-Identifier: MIT
#
# Copyright The SCons Foundation

def generate(env):
    env['Toolpath_TestTool2'] = 1

def exists(env):
    return 1
