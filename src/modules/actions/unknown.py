#!/usr/bin/python
#
# CDDL HEADER START
#
# The contents of this file are subject to the terms of the
# Common Development and Distribution License (the "License").
# You may not use this file except in compliance with the License.
#
# You can obtain a copy of the license at usr/src/OPENSOLARIS.LICENSE
# or http://www.opensolaris.org/os/licensing.
# See the License for the specific language governing permissions
# and limitations under the License.
#
# When distributing Covered Code, include this CDDL HEADER in each
# file and include the License file at usr/src/OPENSOLARIS.LICENSE.
# If applicable, add the following below this CDDL HEADER, with the
# fields enclosed by brackets "[]" replaced with your own identifying
# information: Portions Copyright [yyyy] [name of copyright owner]
#
# CDDL HEADER END
#

#
# Copyright 2007 Sun Microsystems, Inc.  All rights reserved.
# Use is subject to license terms.
#

"""module describing a unknown packaging object

This module contains the UnknownAction class, which represents a unknown type
of packaging object.  This is used when the client side of the package
publishing transaction is not given enough information to determine what type of
object it is.  No datastreams or attributes aside from a path are stored."""

import generic

class UnknownAction(generic.Action):
        """Class representing a unknown type of packaging object."""

        name = "unknown"
        attributes = ("path",)

        def __init__(self, data=None, **attrs):
                generic.Action.__init__(self, data, **attrs)
