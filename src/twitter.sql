-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2021-11-25 15:05:11
-- 服务器版本： 5.7.34-log
-- PHP 版本： 7.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `pigeon`
--

-- --------------------------------------------------------

--
-- 表的结构 `twitter`
--

CREATE TABLE `twitter` (
  `nick` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '昵称',
  `twitter` varchar(3200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '留言内容',
  `time` datetime NOT NULL COMMENT '时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- 转存表中的数据 `twitter`
--

INSERT INTO `twitter` (`nick`, `twitter`, `time`) VALUES
('东方幻梦', 'TEST', '2021-11-25 15:04:36');

--
-- 转储表的索引
--

--
-- 表的索引 `twitter`
--
ALTER TABLE `twitter`
  ADD PRIMARY KEY (`time`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
