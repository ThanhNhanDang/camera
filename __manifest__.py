{
    # Tên module
    'name': 'Camera Odoo 17.0',
    'version': '1.0',
    "author": "NhanDT",
    # Loại module
    'category': 'Camera',

    # Độ ưu tiên module trong list module
    # Số càng nhỏ, độ ưu tiên càng cao
    # Chấp nhận số âm
    'sequence': 5,

    # Mô tả module
    'summary': 'Module này để các bạn tích hợp camera vào việc chụp hình',
    'description': '',


    # Module dựa trên các category nào
    # Khi hoạt động, category trong 'depends' phải được install
    # rồi module này mới đc install
    'depends': ['base_setup'],

    # Module có được phép install hay không
    # Nếu bạn thắc mắc nếu tắt thì làm sao để install
    # Bạn có thể dùng 'auto_install'
    'installable': True,
    'auto_install': False,
    'application': True,

    # Import các file cấu hình
    # Những file ảnh hưởng trực tiếp đến giao diện (không phải file để chỉnh sửa giao diện)
    # hoặc hệ thống (file group, phân quyền)
    'data': [
        'security/ir.model.access.csv',
        "views/res_partner_inherit.xml"
    ],

    # Import các file cấu hình (chỉ gọi từ folder 'static')
    # Những file liên quan đến
    # + các class mà hệ thống sử dụng
    # + các chỉnh sửa giao diện
    # + t
    'assets': {
        'web.assets_backend': [
            'camera/static/src/**/*',
        ],
    },
    'license': 'LGPL-3',

    # 'assets': {
    # 'web.assets_backend': [
    #     'hello_world/static/src/js/settings.js',
    #     ],
    # },

}
