#include <ros/ros.h>
#include <std_msgs/Int32.h>

int main(int argc, char **argv)
{

    ros::init(argc, argv, "signal");
    ros::NodeHandle n;

    ros::Publisher signal_pub = n.advertise<std_msgs::Int32>("/Signal", 1000);

    ros::Rate loop_rate(1);
    int cnt = 0;
    while (ros::ok())
    {
        std_msgs::Int32 msg;
        msg.data = 0;
        if(cnt == 2){
            cnt = 0;
            if(msg.data == 0)msg.data = 1;
            else if(msg.data == 1)msg.data = 0;
        }
        signal_pub.publish(msg);
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}