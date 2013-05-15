# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'build_msi',
      'type': 'none',
      'dependencies': [
#        'dart.gyp:create_sdk'
      ],
      'actions': [
        {
          'action_name': 'heat_dart_sdk',
          'inputs': [
            '<(PRODUCT_DIR)/dart-sdk/README',
          ],
          'outputs': [
            '<(PRODUCT_DIR)/dart-sdk.wxs',
          ],
          'action': [
            '../../third_party/wix37/heat.exe',
            'dir', '<(PRODUCT_DIR)/dart-sdk',
            '-gg',
            '-cg', 'DartSDK',
            '-o', '<(PRODUCT_DIR)/dart-sdk.wxs',
            '-var', 'var.MySource',
          ],          
          'message': 'Creating MSI.',
        },
        {
          'action_name': 'candle_dart_sdk_wxs',
          'inputs': [
            '<(PRODUCT_DIR)/dart-sdk.wxs',
          ],
          'outputs': [
            '<(PRODUCT_DIR)/dart-sdk.wixobj',
          ],
          'action': [
            '../../third_party/wix37/candle.exe',
            '-dMySource=<(PRODUCT_DIR)\dart-sdk',
            '<(PRODUCT_DIR)/dart-sdk.wxs',
            '-out', '<(PRODUCT_DIR)/dart-sdk.wixobj',
          ],
        },
        {
          'action_name': 'candle_dart_wxs',
          'inputs': [
            'dart.wxs',
          ],
          'outputs': [
            '<(PRODUCT_DIR)/dart.wixobj',
          ],
          'action': [
            '../../third_party/wix37/candle.exe',
            'dart.wxs',
            '-dMySource=<(PRODUCT_DIR)\dart-sdk',
            '-out', '<(PRODUCT_DIR)/dart.wixobj',
          ],
        },
        {
          'action_name': 'light_dart',
          'inputs': [
            '<(PRODUCT_DIR)/dart.wixobj',
            '<(PRODUCT_DIR)/dart-sdk.wixobj',
          ],
          'outputs': [
            '<(PRODUCT_DIR)/dart.msi',
          ],
          'action': [
            '../../third_party/wix37/light.exe',
            '<(PRODUCT_DIR)/dart.wixobj',
            '<(PRODUCT_DIR)/dart-sdk.wixobj',
            '-o', '<(PRODUCT_DIR)/dart.msi',
            '-ext', 'WixUIExtension',
          ],
        },        
      ],
    },
  ],
}
