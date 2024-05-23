from setuptools import find_packages, setup

package_name = 'motor_control_serial_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='totomylt',
    maintainer_email='totomylt@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_control = motor_control_serial_pub.motor_control:main',
            'body_control = motor_control_serial_pub.body_control:main'
        ],
    },
)
