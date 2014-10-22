# -*- coding: utf-8 -*-
#
# A framework of sentiment analysis applied on the tweets related to the 2014 FIFA World Cup.
# Copyright (C) 2014 Rubens Pessoa 
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#

from django.db import models

class Tweet(models.Model):
    tweet = models.TextField()

    def __unicode__(self):
        return self.tweet
    
class Tweet_Parsed(models.Model):
    tweet_parsed = models.TextField()

    def __unicode__(self):
        return self.tweet_parsed
    
class Score(models.Model):
    score = models.IntegerField()

    def __unicode__(self):
        return self.score