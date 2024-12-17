# -*- coding: utf-8 -*-
"""
Created on 2024-12-13 18:31:37

@author: .v, Chairman of sigma.lab.

I hope to use AI or LLMs to help people better understand the world and humanity.

We are big fans of xAI.

I am recently interested in MLLMs' safety and Multi-Agent.
"""

import torch.nn.functional as F
import torch


a = F.log_softmax(torch.randn(1, 3, 32, 32), dim=1)
print(a.shape)

