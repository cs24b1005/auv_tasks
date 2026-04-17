from setuptools import find_packages, setup

package_name = 'my_chat_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/msg', ['msg/BotPose.msg']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vboxuser',
    maintainer_email='vboxuser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        	'chat = my_chat_pkg.task1:main',
        	'signal_pub = my_chat_pkg.signal_publisher:main',
        	'signal_proc = my_chat_pkg.signal_processor:main',
        	'signal_out = my_chat_pkg.signal_output:main',
        	'commander = my_chat_pkg.commander:main',          
        	'navigator = my_chat_pkg.navigator:main',
        ],
    },
)
